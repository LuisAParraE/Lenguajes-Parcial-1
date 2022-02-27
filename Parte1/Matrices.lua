
function multMatriz( mA, mB)
    if #mA[1] ~= #mB then
        print("Error las dimensiones de las matrices a multiplicar no coinciden")
        return nil
    end

    mAB = {}
    for i = 1, #mA, 1 do
        mAB[i] = {}
        for j = 1, #mB[1], 1 do
            mult = 0
            for k = 1, #mB, 1 do
                mult = mult + mA[i][k] * mB[k][j]  
            end
            mAB[i][j] = mult
        end
    end

    return mAB
end
function main()

    matrizA = {}
    matrizB = {}

    io.write("Introduzca la cantidad de filas de la Matriz A: ")
    arow = tonumber(io.read())

    io.write("Introduzca la cantidad de columnas de la Matriz A: ")
    acol = tonumber(io.read())

    for i = 1, arow,1 do
        matrizA[i] = {}
        for j =1, acol, 1 do
            io.write("Introduzca valor para posicion [",i,"][",j,"]: ")
            matrizA[i][j] = tonumber(io.read())
        end
    end
    print("\nMatriz A:\n")
    for i = 1, arow,1 do
        for j =1, acol, 1 do
            io.write(matrizA[i][j], " : ") 
        end
        print()
    end

    io.write("Introduzca la cantidad de filas de la Matriz B: ")
    brow = tonumber(io.read())

    io.write("Introduzca la cantidad de columnas de la Matriz B: ")
    bcol = tonumber(io.read())

    for i = 1, brow,1 do
        matrizB[i] = {}
        for j =1, bcol, 1 do
            io.write("Introduzca valor para posicion [",i,"][",j,"]: ")
            matrizB[i][j] = tonumber(io.read())
        end
    end

    print("\nMatriz B:\n")
    for i = 1, brow,1 do
        for j =1, bcol, 1 do
            io.write(matrizB[i][j], " : ") 
        end
        print()
    end
    print("\nEl resultado es:\n")
    producto = multMatriz(matrizA,matrizB)
    if producto ~= nil then
        for i = 1, #producto,1 do
            for j =1, #producto[1], 1 do
                io.write(producto[i][j], " : ") 
            end
            print()
        end
    end
end

main()