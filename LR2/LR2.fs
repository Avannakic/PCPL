let getTupleFromTuple (a, b) = 
    (a + b, a * b)

let getTupleCurried a b = 
    (a + b, a * b)


let rec sumRange a b =
    if a > b then 0
    else a + sumRange (a + 1) b


let sumRangeTail a b =
    let rec loop current max acc =
        if current > max then acc
        else loop (current + 1) max (acc + current)
    loop a b 0


let rec stateA (str: string) =
    if str = "" then 
        "Остановка в A"
    elif str.StartsWith("A") then 
        stateB (str.Substring(1))
    else 
        "Ошибка: ожидалась буква A"

and stateB (str: string) =
    if str = "" then 
        "Остановка в B"
    elif str.StartsWith("B") then 
        stateC (str.Substring(1)) 
    else 
        "Ошибка: ожидалась буква B"

and stateC (str: string) =
    if str = "" then 
        "Остановка в C"
    elif str.StartsWith("C") then 
        stateA (str.Substring(1)) 
    else 
        "Ошибка: ожидалась буква C"


let sum = fun x y z -> x + y + z

let applyTuple (x, y, z) func = 
    func x y z

let applyCurried x y z func = 
    func x y z

[<EntryPoint>]
let main _ =
    printfn "--- Задача 1 ---"
    printfn "Кортеж (5, 3): %A" (getTupleFromTuple (5, 3))
    printfn "Каррирование 5 3: %A" (getTupleCurried 5 3)

    printfn "\n--- Задача 2 и 3 ---"
    printfn "Обычная рекурсия (сумма 1..5): %d" (sumRange 1 5)
    printfn "Хвостовая рекурсия (сумма 1..5): %d" (sumRangeTail 1 5)

    printfn "\n--- Задача 4 (Автомат) ---"
    printfn "Проверка 'ABC': %s" (stateA "ABC")
    printfn "Проверка 'ABCABC': %s" (stateA "ABCABC")
    printfn "Проверка 'AB': %s" (stateA "AB")
    printfn "Проверка 'ABA': %s" (stateA "ABA")

    printfn "\n--- Задача 5 ---"
    printfn "Лямбда через кортеж (1, 2, 3): %d" (applyTuple (1, 2, 3) sum)
    printfn "Лямбда через каррирование 1 2 3: %d" (applyCurried 1 2 3 sum)

    0
