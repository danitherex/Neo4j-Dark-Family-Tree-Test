from neo4j import GraphDatabase
from enums import Relationships,Genders

class FamilyTree:
    def __init__(self,uri,username,password):
        self.driver = GraphDatabase.driver(uri=uri, auth=(username,password))
        self.driver.verify_connectivity()

    
    def create_member(self,name:str,gender:Genders, relationship:Relationships=None, relationship_to:str=None):
        with self.driver.session() as session:
            session.run(f"MERGE(m:Member:{gender.name} {{name:$name}}) RETURN m",name=name)
            print(f"Member {name} created")
        if relationship and relationship_to:
            self.create_relationship(name,relationship,relationship_to)
    
    def create_relationship(self,name:str,relationship:Relationships,relationship_to:str):
        with self.driver.session() as session:
            query = f'''
                MATCH (m:Member {{name:$name}})
                MATCH (rel_to:Member {{name:$relationship_to}})
                CREATE (m)-[:{relationship.name}]->(rel_to)
            '''
            print(query)
            session.run(query,name=name,relationship_to=relationship_to)
            print(f"Relationship between {name} and {relationship_to} created")
    def close(self):
        self.driver.close()