function power(base, potencia)
    if potencia == 0 then
        return  1
    else 
        return (base * power(base, potencia-1))
    end
    
end

while true do
    io.write("Introduzca la base del numero: ")
    a = tonumber(io.read())

    if a < 0 then
        print("Error, numero negativo")
    else
        break
    end
        
end

while true do
    io.write("Introduzca la potencia del numero: ")
    b = tonumber(io.read())

    if b < 0 then
        print("Error, numero negativo")
    else
        break
    end

end

print(a)
print(b)
print(power(a,b))
