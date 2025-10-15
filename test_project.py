# test_project.py
import unittest
from project_code import avg_body_mass_by_species_sex, avg_flipper_by_species_island

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        #sample text examples to run 
        self.SAMPLE = [
            # Adelie on Torgersen (male and female)
            {"species":"Adelie","island":"Torgersen","bill_length_mm":"38.6","bill_depth_mm":"21.2",
             "flipper_length_mm":"191","body_mass_g":"3800","sex":"male","year":"2007"},
            {"species":"Adelie","island":"Torgersen","bill_length_mm":"36.6","bill_depth_mm":"17.8",
             "flipper_length_mm":"185","body_mass_g":"3700","sex":"female","year":"2007"},
            # Gentoo on Biscoe
            {"species":"Gentoo","island":"Biscoe","bill_length_mm":"46.1","bill_depth_mm":"14.8",
             "flipper_length_mm":"215","body_mass_g":"3500","sex":"male","year":"2008"},
            {"species":"Gentoo","island":"Biscoe","bill_length_mm":"47.5","bill_depth_mm":"15.0",
             "flipper_length_mm":"217","body_mass_g":"NA","sex":"female","year":"2008"}, 
        ]

    # BODY MASS TEST CASES
    def test_avg_mass_for_adelie(self):
        results = {}
        for species_type, species_sex, average in avg_body_mass_by_species_sex(self.SAMPLE):
            results[(species_type, species_sex)] = average
        self.assertEqual(results[("Adelie","male")], 3800) #test male 
        self.assertEqual(results[("Adelie","female")], 3700) #test female 

    def test_avg_mass_gentoo(self):
        results = {}
        for species_type, species_sex, average in avg_body_mass_by_species_sex(self.SAMPLE):
            results[(species_type, species_sex)] = average
        self.assertEqual(results[("Gentoo","male")], 3500) #test male 
        self.assertNotIn(("Gentoo","female"), results)  # test female (NA)

    def test_avg_mass_single_row(self):
        data = [self.SAMPLE[1]]  # make sure handles small iput correctly 
        self.assertEqual(avg_body_mass_by_species_sex(data), [("Adelie","female",3700)])

    def test_avg_mass_empty(self): #make sure handle empty list correctly 
        self.assertEqual(avg_body_mass_by_species_sex([]), [])

    # FLIPPER LENGTH TEST CASES
    def test_avg_flipper_adelie_torgersen(self):
        results = {}
        for species_type, island, average in avg_flipper_by_species_island(self.SAMPLE):
            results[(species_type, island)] = average
        self.assertEqual(results[("Adelie","Torgersen")], 188)  #taking male and female and dividing

    def test_avg_flipper_gentoo_biscoe(self):
        results = {}
        for species_type, island, average in avg_flipper_by_species_island(self.SAMPLE):
            results[(species_type, island)] = average
        self.assertEqual(results[("Gentoo","Biscoe")], 216)  #taking male and female and dividing

    def test_avg_flipper_rows(self):
        data = [self.SAMPLE[1]]  # make sure handles small iput correctly 
        self.assertEqual(avg_flipper_by_species_island(data), [("Adelie","Torgersen",185)])

    def test_avg_flipper_empty(self):
        self.assertEqual(avg_flipper_by_species_island([]), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
