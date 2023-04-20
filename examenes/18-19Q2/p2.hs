exps :: Float -> [Float]
exps x = exps'
    where
        exps' = 1:zipWith (\acc i -> acc * x / i) exps' [1..]

exponencial :: Float -> Float -> Float
exponencial x err = sum $ takeWhile (>=err) $ exps x