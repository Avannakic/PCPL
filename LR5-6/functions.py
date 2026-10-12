from random import choice
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton

from states import BotStates
from keyboards import get_menu_kb, get_settings_kb, get_test_kb, get_back_menu_kb,get_result_kb
from words_dict import wordsdict

async def start(message: types.Message, state: FSMContext):
    await state.set_state(BotStates.menu)
    await state.update_data(active_categories=list(wordsdict.keys()))
    await message.answer("Выбери, что тебя интересует", reply_markup=get_menu_kb())

async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.menu)
    data = await state.get_data()

    text = "Выбери, что тебя интересует"
    total = data.get("total_questions", 0)

    if total > 0:
        correct = data.get("correct_answers", 0)
        text = f"Тест прерван.\nТвой результат: {correct} из {total} верных ответов.\n" + text

        await state.update_data(testwords=[], correct_answers=0, total_questions=0)
    await call.message.edit_text(text, reply_markup=get_menu_kb())
    await call.answer()

async def enter_settings(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.settings)
    data = await state.get_data()
    active_categories = data.get("active_categories", list(wordsdict.keys()))
    await call.message.edit_text("Выберите категории слов для теста:", reply_markup=get_settings_kb(active_categories))
    await call.answer()

async def toggle_category(call: types.CallbackQuery, state: FSMContext):
    cat_key = call.data.split("_")[1]

    data = await state.get_data()
    active_categories = data.get("active_categories", list(wordsdict.keys()))

    if cat_key in active_categories:
        active_categories.remove(cat_key)
    else:
        active_categories.append(cat_key)

    await state.update_data(active_categories=active_categories)
    await call.message.edit_reply_markup(reply_markup=get_settings_kb(active_categories))
    await call.answer()

async def end_settings(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.menu)
    await call.message.edit_text(
        "Список слов выбран, вы можете приступить к тесту",
        reply_markup=get_menu_kb()
    )
    await call.answer()


async def ask_question(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.testing)
    data = await state.get_data()

    active_categories = data.get("active_categories", list(wordsdict.keys()))
    testwords = data.get("testwords", [])

    if not testwords:
        for cat in active_categories:
            testwords.extend(wordsdict.get(cat, []))
        await state.update_data(testwords=testwords, correct_answers=0, total_questions=0)

    word = choice(testwords)
    base_word, *comment_parts = word.split("(")
    comment = f"({comment_parts[0]}" if comment_parts else ""

    vowels = "АЕЁИОУЫЭЮЯаеёиоуыэюя"
    buttons = []

    for i, char in enumerate(base_word):
        if char in vowels:
            variant = base_word.lower()
            variant = variant[:i] + variant[i].upper() + variant[i + 1:]
            full_variant = variant + comment

            is_right = "right" if full_variant == word else "wrong"
            buttons.append(
                [InlineKeyboardButton(text=full_variant, callback_data=f"ans_{is_right}_{word}")]
            )

    await call.message.edit_text("Выберите верный вариант ответа:", reply_markup=get_test_kb(buttons))
    await call.answer()


async def check_answer(call: types.CallbackQuery, state: FSMContext):
    _, action, original_word = call.data.split("_", 2)

    data = await state.get_data()
    testwords = data.get("testwords", [])
    correct = data.get("correct_answers", 0)
    total = data.get("total_questions", 0)

    total += 1

    if action == "wrong":
        text = f"❌ Неверно!\nПравильный ответ: {original_word}"
    else:
        correct += 1
        text = f"✅ Верно!\nПравильный ответ: {original_word}"
        if original_word in testwords:
            testwords.remove(original_word)

    if len(testwords) == 0:
        text += f"\n🎉 Вы изучили все слова!\nВаш итоговый результат: {correct} из {total}.\nДля того чтобы снова начать тест, вернитесь в меню"
        await state.update_data(testwords=[], correct_answers=0, total_questions=0)
        await call.message.edit_text(text, reply_markup=get_result_kb(is_empty=True))
    else:
        await state.update_data(testwords=testwords, correct_answers=correct, total_questions=total)
        await call.message.edit_text(text, reply_markup=get_result_kb(is_empty=False))
    await call.answer()

async def to_list(call:types.CallbackQuery):
    list_btn = InlineKeyboardButton(text="Полный орфоэпический словник",
                                    url="https://4ege.ru/russkiy/71318-slovnik-orfoepicheskij-ege.html?ysclid=muloair2ao136122164")
    await call.message.edit_text("На этом сайте вы сможете найти полный орфоэпический словник и скачать его pdf-версию:",
                                 reply_markup=get_back_menu_kb(list_btn))
    await call.answer()

async def enter_help(call: types.CallbackQuery):
    await call.message.edit_text(
        "Если у вас появилось предложение по улучшению бота/вы нашли какую-то ошибку, обращайтесь! @OrphoEGE_support",
        reply_markup=get_back_menu_kb())
    await call.answer()