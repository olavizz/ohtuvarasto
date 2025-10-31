import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(-10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_varastolla_positiivinen_tilavuus(self):
        varasto = Varasto(-5)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_positiivinen_saldo(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)
    
    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liika_lisaaminen_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(30)

        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_negatiivinen_ottaminen_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-20)

        self.assertAlmostEqual(saatu_maara, 0)
    
    def test_liika_ottaminen_palauttaa_kaiken(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(20)

        self.assertAlmostEqual(saatu_maara, 8)
    
    def test_print_palauttaa_saldon_ja_jaljella_olevan_tilan(self):
        self.varasto.lisaa_varastoon(4)

        self.assertEqual(str(self.varasto), "saldo = 4, vielä tilaa 6")
