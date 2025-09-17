var1=10
var2=20

func_global() {
    var1=100
    var2=200
    echo "Function global Calls the global variables: Var 1: ${var1}, Var 2: ${var2}"
}

func_local() {
    local var1=-100
    local var2=-200
    echo "Function local Calls the local variables: Var 1: ${var1}, Var 2: ${var2}"
}

echo "Var 1: ${var1} and Var 2: ${var2}"
func_global
echo "After Func Global Funcion call: Var 1: ${var1} and Var 2: ${var2}"
func_local
