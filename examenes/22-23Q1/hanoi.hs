main :: IO ()  
main = do 
    input <- getLine
    resultat input

resultat :: String -> IO ()
resultat linia = hanoi num ori aux dest
    where
        [col, ori, aux, dest] = words linia
        num = read col :: Int

hanoi :: Int -> String -> String -> String -> IO ()
hanoi 0 _ _ _ = return ()
hanoi n o d a = do
    hanoi (n-1) o a d --move n-1 from origin to aux
    putStrLn (o ++ " -> " ++ d) --move biggest one from origin to dest
    hanoi (n-1) a d o --move n-1 from aux to dest
    