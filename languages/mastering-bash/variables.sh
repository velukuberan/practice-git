#!/bin/bash

MY_TERM=$TERM
echo "First Way: TTY Term: " $MY_TERM
echo "Second Way: TTY Term: ${MY_TERM}"

fruits=(apple pear banana)
echo "${fruits[0]}, ${fruits[2]} ${#fruits[2]}"
