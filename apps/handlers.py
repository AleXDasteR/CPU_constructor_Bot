from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import apps.built_PCs as bPC
import apps.keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()


class Combination(StatesGroup):
    budget = State()
    cpu = State()
    gpu = State()


@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(
        'Привет! Я - бот-помощник по сборке комплектующих для компьютера\n' +
        '\nЯ помогу тебе собрать лучший компьютер в ценовом диапазоне и на выбранной архитектуре!\n\n' +
        'Выбирай ценовой диапазон из списка ниже:',
        reply_markup=kb.main_prices)


@router.message(Command('help'))
async def help_command(message: Message):
    await message.answer('Выбери архитектуру для сборки компьютера или же производителя чипов. AMD/Intel',
                         )


@router.callback_query(F.data == 'budget')
async def budget_pc(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Combination.budget)
    await callback.answer()
    await callback.message.edit_text('Мы собираем бюджетный компьютер, теперь выбери платформу для своего компьютера:',
                                     reply_markup=kb.main)
    await state.update_data(budget=0)


@router.callback_query(F.data == 'mid-budget')
async def budget_pc(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Combination.budget)
    await callback.answer()
    await callback.message.edit_text(
        'Мы собираем среднебюджетный компьютер, теперь выбери платформу для своего компьютера:',
        reply_markup=kb.main)
    await state.update_data(budget=1)


@router.callback_query(F.data == 'high-end-budget')
async def budget_pc(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Combination.budget)
    await callback.answer()
    await callback.message.edit_text('Мы собираем мажорский компьютер, теперь выбери платформу для своего компьютера:',
                                     reply_markup=kb.main)
    await state.update_data(budget=2)


@router.callback_query(F.data == 'AMD_CPU')
async def amd_choice(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Ты выбрал AMD в качестве процессора - теперь надо выбрать сокет AM4 или AM5',
        reply_markup=kb.main_AMD)


@router.callback_query(F.data == 'AM4_CPU')
async def am4_choice(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Combination.cpu)
    await callback.answer()
    await callback.message.edit_text('Ты выбрал сокет АМ4 - осталась только видеокарта, какой бренд ты выберешь?',
                                     reply_markup=kb.main_GPU)
    await state.update_data(cpu='am4')


@router.callback_query(F.data == 'AM5_CPU')
async def am5_choice(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Combination.cpu)
    await callback.answer()
    await callback.message.edit_text('Ты выбрал сокет АМ5 - осталась только видеокарта, какой бренд ты выберешь?',
                                     reply_markup=kb.main_GPU)
    await state.update_data(cpu='am5')


@router.callback_query(F.data == 'INTEL_CPU')
async def intel_choice(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Combination.cpu)
    await callback.answer()
    await callback.message.edit_text('Ты выбрал сокет LGA 1700(Intel) - осталась только видеокарта,' +
                                     ' какой бренд ты выберешь?',
                                     reply_markup=kb.main_GPU)
    await state.update_data(cpu='intel')


@router.callback_query(F.data == 'Nvidia_GPU')
async def nvidia_choice(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Combination.gpu)
    await callback.answer()
    await callback.message.edit_text('Ты выбрал видеокарту от Nvidia - ' +
                                     'всё готово нажми на кнопку ниже, чтобы узнать итоговую сборку',
                                     reply_markup=kb.output_PC)
    await state.update_data(gpu='nvidia')


@router.callback_query(F.data == 'AMD_GPU')
async def amd_gpu_choice(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Combination.gpu)
    await callback.answer()
    await callback.message.edit_text('Ты выбрал видеокарту от AMD - ' +
                                     'всё готово нажми на кнопку ниже, чтобы узнать итоговую сборку',
                                     reply_markup=kb.output_PC)
    await state.update_data(gpu='amd')


@router.callback_query(F.data == 'output')
async def end_pc(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    cpu_output = bPC.cpus[data["cpu"]][data["budget"]]
    correct_gpu = data["gpu"] + '_' + data["cpu"]
    gpu_output = bPC.gpus[correct_gpu][data["budget"]]
    await callback.answer()
    await callback.message.answer(f'Вот твоя сборка:\nПроцессор - {cpu_output}\nВидеокарта - {gpu_output}')
    await state.clear()
