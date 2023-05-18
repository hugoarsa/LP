main :: IO() = do   
    input <- getLine
    resposta input

resposta :: String -> IO ()
resposta input = hanoi num ori aux dest
    where 
        [num_temp,ori,aux,dest] = words input
        num = (read num_temp) :: Int


hanoi :: Int -> String -> String -> String -> IO ()
hanoi 0 _ _ _ = return ()
hanoi n o d a = do
    hanoi (n-1) o a d --move n-1 from origin to aux
    putStrLn (o ++ " -> " ++ d) --move biggest one from origin to dest
    hanoi (n-1) a d o --move n-1 from aux to dest
    