divisors :: Int -> [Int]
divisors a = [1]++[x | x <- [1..a], x `mod` a == 0]