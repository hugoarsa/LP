divisors :: Int -> [Int]
divisors x = [d | d <- [1..x], mod x d == 0]

nbDivisors :: Int -> Int
nbDivisors = length . divisors

moltCompost :: Int -> Bool
moltCompost n   = null [x | x <- [1..(n-1)], nbDivisors x >= nbDivisors n ] 