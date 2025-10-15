# test_project.py
import unittest
from project_code import average_body_mass_by_species_sex, average_flipper_by_species_island

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        #sample text examples to run 
        self.SAMPLE = [
            # Adelie on Torgersen (male and female)
            {"species":"Adelie","island":"Torgersen","bill_length_mm":"39.1","bill_depth_mm":"18.7",
             "flipper_length_mm":"190","body_mass_g":"3700","sex":"male","year":"2007"},
            {"species":"Adelie","island":"Torgersen","bill_length_mm":"40.2","bill_depth_mm":"18.1",
             "flipper_length_mm":"192","body_mass_g":"3800","sex":"female","year":"2007"},
            # Gentoo on Biscoe (male and add skip NA because GENAI told me this was an important test case to run)
            {"species":"Gentoo","island":"Biscoe","bill_length_mm":"46.1","bill_depth_mm":"14.8",
             "flipper_length_mm":"215","body_mass_g":"5000","sex":"male","year":"2008"},
            {"species":"Gentoo","island":"Biscoe","bill_length_mm":"47.5","bill_depth_mm":"15.0",
             "flipper_length_mm":"217","body_mass_g":"NA","sex":"female","year":"2008"},
        ]

    # test average_body_mass_by_species_sex
    def test_avg_mass_adelie(self):
        res = {(species_type, species_sex): average for (species_type, species_sex, average) in average_body_mass_by_species_sex(self.SAMPLE)}
        self.assertEqual(res[("Adelie","male")], 3700) #test male 
        self.assertEqual(res[("Adelie","female")], 3800) #test female 

    def test_avg_mass_gentoo(self): #however a skipped row 
        res = {(species_type, species_sex): average for (species_type, species_sex, average) in average_body_mass_by_species_sex(self.SAMPLE)}
        self.assertEqual(res[("Gentoo","male")], 5000) #test male 
        self.assertNotIn(("Gentoo","female"), res)  # test female (NA)

    def test_avg_mass_single_row(self):
        data = [self.SAMPLE[0]]  # make sure handles small iput correctly 
        self.assertEqual(average_body_mass_by_species_sex(data), [("Adelie","male",3700)])

    def test_avg_mass_empty(self): #make sure handle empty list correctly 
        self.assertEqual(average_body_mass_by_species_sex([]), [])

    # ---------- average_flipper_by_species_island ----------
    def test_avg_flipper_adelie_torgersen(self):
        res = { (species_type, island): average for (species_type, island, average) in average_flipper_by_species_island(self.SAMPLE) }
        self.assertEqual(res[("Adelie","Torgersen")], 191)  #taking male and female and dividing

    def test_avg_flipper_gentoo_biscoe(self):
        res = { (species_type, island): average for (species_type, island, average) in average_flipper_by_species_island(self.SAMPLE) }
        self.assertEqual(res[("Gentoo","Biscoe")], 216)  #taking male and female and dividing

    def test_avg_flipper_NA_rows(self):
        data = [{"species":"Gentoo","island":"Biscoe","bill_length_mm":"46.1","bill_depth_mm":"14.8",
             "flipper_length_mm":"NA","body_mass_g":"5000","sex":"male","year":"2008"}]
        self.assertEqual(average_flipper_by_species_island(data), [])

    def test_avg_flipper_empty(self):
        self.assertEqual(average_flipper_by_species_island([]), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
