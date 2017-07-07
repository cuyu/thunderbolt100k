#!/usr/bin/env bash
zsh_weather() {
    # Read the cached weather info
    weather=$(< "/tmp/thunderbolt100k_weather.data")
    local weather temp condition color symbol
    # `jq` is required to install
    temp=$(echo $weather | jq .current.temp_c)
    condition=$(echo $weather | jq .current.condition.text)
    # Default value
    color="%F{green}"
    symbol="\uf2c7"

    if [[ $condition == *"rain"* ]] ;
    then symbol="\uf043" ; color='%F{blue}'
    fi

    if [[ $condition == *"cloudy"* || $condition == *"Overcast"* ]] ;
    then symbol="\uf0c2" ; color='%F{white}';
    fi

    if [[ $condition == *"Sunny"* ]] ;
    then symbol="\uf185" ; color='%F{yellow}';
    fi

    echo -n "%{$color%}$symbol  %{%F{grey}%}$temp\uf2c9"
}