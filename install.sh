#!/usr/bin/env bash

zshrc_content=`cat ~/.zshrc`
if [[ $zshrc_content == *"THUNDERBOLT100K"* ]]; then
    echo "THUNDERBOLT100K has been installed."
    exit
fi
# Add new line
echo "" >> ~/.zshrc
echo "############################" >> ~/.zshrc
echo "# For THUNDERBOLT100K" >> ~/.zshrc
# Copy shell functions of each widget into .zshrc
for f in src/*.sh
do
    cat $f >> ~/.zshrc
done

echo "Installation almost done."
echo "Here are some questions you should answer (you may skip and configure them manually by press 'enter' directly):"
echo "Please input your api key for weather: "
read token
echo "" >> ~/.zshrc
echo "THUNDERBOLT100K_WEATHER_TOKEN=$token" >> ~/.zshrc
echo "Please input the city of your location (e.g. Shanghai): "
read city
echo "THUNDERBOLT100K_WEATHER_CITY=$city" >> ~/.zshrc

echo "THUNDERBOLT100K is installed successfully"
echo "You may still need to edit the 'POWERLEVEL9K_LEFT_PROMPT_ELEMENTS' or 'POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS' in
 '~/.zshrc' file to enable the widgets."
echo "If you want to set configurations for THUNDERBOLT100K, please refer to https://github.com/cuyu/thunderbolt100k#configuration"