from family_tree import FamilyTree
from enums import Genders,Relationships


uri="bolt://localhost:7687"
username="neo4j"
password="password"
DarkFamilyTree = FamilyTree(uri,username,password)

DarkFamilyTree.create_member("Noah",Genders.Male)

DarkFamilyTree.create_member("Bernd Doppler",Genders.Male,"Helge Doppler")
DarkFamilyTree.create_member("Greta Doppler",Genders.Female,Relationships.Married_to,"Bernd Doppler")
DarkFamilyTree.create_member("Helge Doppler",Genders.Male,Relationships.Child_of,"Bernd Doppler")
DarkFamilyTree.create_relationship("Helge Doppler",Relationships.Child_of,"Greta Doppler")
DarkFamilyTree.create_member("Peter Doppler",Genders.Male,Relationships.Child_of,"Helge Doppler")
DarkFamilyTree.create_member("Charlotte Doppler",Genders.Female,Relationships.Married_to,"Peter Doppler")
DarkFamilyTree.create_member("Franziska Doppler",Genders.Female,Relationships.Child_of,"Charlotte Doppler")
DarkFamilyTree.create_relationship("Franziska Doppler",Relationships.Child_of,"Peter Doppler")
DarkFamilyTree.create_member("Elisabeth Doppler",Genders.Female,Relationships.Child_of,"Charlotte Doppler")
DarkFamilyTree.create_relationship("Elisabeth Doppler",Relationships.Child_of,"Peter Doppler")
DarkFamilyTree.create_relationship("Charlotte Doppler",Relationships.Child_of,"Elisabeth Doppler")
DarkFamilyTree.create_relationship("Charlotte Doppler",Relationships.Child_of,"Noah")

DarkFamilyTree.create_member("Agnes Nielsen",Genders.Female)
DarkFamilyTree.create_member("Tronte Nielsen",Genders.Male,Relationships.Child_of,"Agnes Nielsen")
DarkFamilyTree.create_member("Jana Nielsen",Genders.Female,Relationships.Married_to,"Tronte Nielsen")
DarkFamilyTree.create_member("Ulrich Nielsen",Genders.Male,Relationships.Child_of,"Tronte Nielsen")
DarkFamilyTree.create_relationship("Ulrich Nielsen",Relationships.Child_of,"Jana Nielsen")
DarkFamilyTree.create_member("Mads Nielsen",Genders.Male,Relationships.Child_of,"Tronte Nielsen")
DarkFamilyTree.create_relationship("Mads Nielsen",Relationships.Child_of,"Jana Nielsen")
DarkFamilyTree.create_member("Katharina Nielsen",Genders.Female,Relationships.Married_to,"Ulrich Nielsen")
DarkFamilyTree.create_member("Magnus Nielsen",Genders.Male,Relationships.Child_of,"Katharina Nielsen")
DarkFamilyTree.create_relationship("Magnus Nielsen",Relationships.Child_of,"Ulrich Nielsen")
DarkFamilyTree.create_member("Martha Nielsen",Genders.Female,Relationships.Child_of,"Katharina Nielsen")
DarkFamilyTree.create_relationship("Martha Nielsen",Relationships.Child_of,"Ulrich Nielsen")
DarkFamilyTree.create_member("Mikkel Nielsen",Genders.Male,Relationships.Child_of,"Katharina Nielsen")
DarkFamilyTree.create_relationship("Mikkel Nielsen",Relationships.Child_of,"Ulrich Nielsen")
DarkFamilyTree.create_member("Hannah Kruger",Genders.Female,Relationships.Married_to,"Mikkel Nielsen")

DarkFamilyTree.create_member("Daniel Kahnwald",Genders.Male)
DarkFamilyTree.create_member("Ines Kahnwald",Genders.Female,Relationships.Child_of,"Daniel Kahnwald")
DarkFamilyTree.create_member("Jonas Kahnwald",Genders.Male,Relationships.Child_of,"Hannah Kruger")
DarkFamilyTree.create_relationship("Jonas Kahnwald",Relationships.Child_of,"Mikkel Nielsen")

DarkFamilyTree.create_member("Egon Tiedemann",Genders.Male)
DarkFamilyTree.create_member("Doris Tiedemann",Genders.Female,Relationships.Married_to,"Egon Tiedemann")
DarkFamilyTree.create_member("Claudia Tiedemann",Genders.Female,Relationships.Child_of,"Doris Tiedemann")
DarkFamilyTree.create_relationship("Claudia Tiedemann",Relationships.Child_of,"Egon Tiedemann")
DarkFamilyTree.create_member("Regina Tiedemann",Genders.Female,Relationships.Child_of,"Claudia Tiedemann")
DarkFamilyTree.create_relationship("Regina Tiedemann",Relationships.Child_of,"Bernd Doppler")
DarkFamilyTree.create_member("Aleksander Tiedemann",Genders.Male,Relationships.Married_to,"Regina Tiedemann")
DarkFamilyTree.create_member("Bartosz Tiedemann",Genders.Male,Relationships.Child_of,"Regina Tiedemann")
DarkFamilyTree.create_relationship("Bartosz Tiedemann",Relationships.Child_of,"Aleksander Tiedemann")



DarkFamilyTree.close()