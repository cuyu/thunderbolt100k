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

echo "THUNDERBOLT100K is installed successfully"
echo "You may still need to edit the 'POWERLEVEL9K_LEFT_PROMPT_ELEMENTS' or 'POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS' in
 '~/.zshrc' file to enable the widgets."
echo "Also don't forget to set necessary configuration for THUNDERBOLT100K (Pls refer to https://github.com/cuyu/thunderbolt100k#configuration)"