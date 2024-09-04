from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardMarkup, KeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main_prices = InlineKeyboardMarkup(inline_keyboard=
                                   [[InlineKeyboardButton(text='Бюджетный', callback_data='budget')],
                                    [InlineKeyboardButton(text='Среднебюджетный', callback_data='mid-budget')],
                                    [InlineKeyboardButton(text='Высокобюджетный', callback_data='high-end-budget')]])
main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='AMD', callback_data='AMD_CPU'),
                                              InlineKeyboardButton(text='Intel', callback_data='INTEL_CPU')]])
main_AMD = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='AM4', callback_data='AM4_CPU'),
                                                  InlineKeyboardButton(text='AM5', callback_data='AM5_CPU')]])

main_GPU = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Nvidia', callback_data='Nvidia_GPU')],
                                                 [InlineKeyboardButton(text='AMD', callback_data='AMD_GPU')]])
output_PC = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Узнать сборку', callback_data='output')]])
