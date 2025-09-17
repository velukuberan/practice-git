func1() {
    echo "This is func1 under your command sir."
    return $((10 + 11))
    # echo "This is func1 under your command sir."
    # return $((2020 + 11))
}

fun2() {
    echo "File is writeable" >>outputFunc2.txt
    if [$? -ne 0]; then
        echo "41"
    else
        echo "40"
    fi
}

func1
# echo "fun fun fun"
echo "Will this buddy func1 returns any value? Yes sir, it seems to be: => $?"
fun2
