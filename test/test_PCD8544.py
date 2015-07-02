import unittest

from mock import Mock, call

import CardosoTech_GPIO.SPI as SPI
import CardosoTech_LCD_Shield as LCD


class TestPCD8544(unittest.TestCase):
	def test_command_sets_dc_low(self):
		gpio = Mock()
		spi = Mock()
		lcd = LCD.PCD8544(1, 2, gpio=gpio, spi=spi)
		lcd.command(0xDE)
		gpio.set_low.assert_called_with(1)
		spi.write.assert_called_with([0xDE])

	def test_data_sets_dc_high(self):
		gpio = Mock()
		spi = Mock()
		lcd = LCD.PCD8544(1, 2, gpio=gpio, spi=spi)
		lcd.data(0xDE)
		gpio.set_high.assert_called_with(1)
		spi.write.assert_called_with([0xDE])

	def test_default_to_bitbang_spi(self):
		gpio = Mock()
		lcd = LCD.PCD8544(1, 2, 3, 4, 5, gpio=gpio)
		lcd.begin()
		self.assertIsInstance(lcd._spi, SPI.BitBang)

	def test_begin_initializes_lcd(self):
		gpio = Mock()
		spi = Mock()
		lcd = LCD.PCD8544(1, 2, gpio=gpio, spi=spi)
		lcd.begin(40)
		# Verify RST is set low then high.
		gpio.assert_has_calls([call.set_low(2), call.set_high(2)])
		# Verify SPI calls.
		spi.assert_has_calls([call.write([0x21]), 
							  call.write([0x14]),
							  call.write([0xA8]),
							  call.write([0x20]),
							  call.write([0x0c])])
