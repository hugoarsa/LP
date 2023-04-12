eval1 :: String -> Int
eval1 expr = sub_eval (words expr) []

sub_eval :: [String] -> [Int] -> Int
sub_eval [] [] = 0 --caso limite de que no me metas nada claramente la respuesta ha de ser 0
sub_eval [] [result] = result --si la primera esta vacía el resultado se encuentra en el primer elemento de la segunda
sub_eval (x:xs) (ys) --caso recursivo
    | x == "+" = sub_eval xs ((a + b):rest)
    | x == "-" = sub_eval xs ((b - a):rest)
    | x == "*" = sub_eval xs ((a * b):rest)
    | x == "/" = sub_eval xs ((div b a):rest)
    | otherwise = sub_eval xs (num:ys)
    where 
        (a:b:rest) = ys
        num = read x :: Int
        

eval2 :: String -> Int
eval2 s = head $ foldl eval2' [] (words s)
    where
        eval2' :: [Int] -> String -> [Int]
        eval2' (a:b:rest) x
            | x == "*"  = [b * a] ++ rest
            | x == "/"  = [div b a] ++ rest
            | x == "+"  = [b + a] ++ rest
            | x == "-"  = [b - a] ++ rest
            | otherwise = [(read  x::Int)] ++ [a, b] ++ rest
        eval2' rest x = [(read  x::Int)] ++ rest

fsmap :: a -> [a -> a] -> a
fsmap a [] = a
fsmap a (f:fs) = fsmap (f a) fs

divideNconquer :: (a -> Maybe b) -> (a -> (a, a)) -> (a -> (a, a) -> (b, b) -> b) -> a -> b
divideNconquer base divide conquer x =
    case base x of
        Just y  -> y
        Nothing -> conquer x (x1, x2) (y1, y2)
            where
                (x1, x2) = divide x
                y1 = divideNconquer base divide conquer x1
                y2 = divideNconquer base divide conquer x2

quickSort :: [Int] -> [Int]
quickSort = divideNconquer base divide conquer
    where
        base [] = Just []
        base [x] = Just [x]
        base _ = Nothing

        divide (x:xs) = (menors, majors)
            where menors = filter (<= x) xs
                  majors = filter (>  x) xs
        --divide (x:xs) = partition (<= x) xs

        conquer (x:_) _ (ys1, ys2) = ys1 ++ [x] ++ ys2


data Racional = Racional Integer Integer

instance Eq Racional where
    (Racional n1 d1) == (Racional n2 d2) = n1 * d2 == n2 * d1

instance Show Racional where
    show (Racional a b) = (show $ div a c) ++ "/" ++ (show $ div b c)
        where
            c = gcd a b
    
racional :: Integer -> Integer -> Racional
racional a b = Racional a b

numerador :: Racional -> Integer
numerador (Racional a b) = div a (gcd a b)

denominador :: Racional -> Integer
denominador (Racional a b) = div b (gcd a b)

data Tree a = Node a (Tree a) (Tree a)
recXnivells :: Tree a -> [a]
recXnivells t = recXnivells' [t]
    where recXnivells' ((Node x fe fd):ts) = x:recXnivells' (ts ++ [fe, fd])

racionals :: [Racional]
racionals = recXnivells (arbreCW (Racional 1 1))

arbreCW :: Racional -> Tree Racional
arbreCW r = Node r (arbreCW (racional a (a + b))) (arbreCW (racional (a + b) b))
    where 
        a = numerador r 
        b = denominador r