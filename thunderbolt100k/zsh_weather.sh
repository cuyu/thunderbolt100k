POWERLEVEL9K_CUSTOM_WEATHER="zsh_weather"
PYTHON_PATH=$(which python)
zsh_weather() {
    echo $($PYTHON_PATH /Users/CYu/Code/Shell/thunderbolt100k/src/zsh_weather.py)
}