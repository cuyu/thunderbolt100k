# thunderbolt100k (In progress)

![screenshot](/screenshot.png)

Build your awesome terminal with [powerlevel9k](https://github.com/bhilburn/powerlevel9k) and this project!

This project is inspired by [JulienLemonde' Configuration](https://github.com/bhilburn/powerlevel9k/wiki/Show-Off-Your-Config#julienlemonde-configuration) for powerlevel9k. The reason I start on this project is that I found it always takes some time to get the weather information each time I press the 'return' button. I want fluent terminal use experience as well as these information displayed and here it is.

### Prerequisites

1. Install [Oh My ZSH](http://ohmyz.sh/)
2. Install [powerlevel9k](https://github.com/bhilburn/powerlevel9k) theme
3. Install [nerd-fonts](https://github.com/ryanoasis/nerd-fonts)

### Installation

Use pip (not ready yet~):

```
pip install thunderbolt100k
```

### Configuration

All the configurations are in the `~/.zshrc`. For example, you can configure the token of https://api.apixu.com, weather location and etc. in `~/.zshrc` file. Here are all the configurations you can set:

```shell
# The token (i.e. api key) for https://api.apixu.com
THUNDERBOLT100K_WEATHER_TOKEN=<ToBeReplaced>
# The city of the weather
THUNDERBOLT100K_WEATHER_CITY=<ToBeReplaced>
# Interval (minutes) to pull the weather info, by default is 5 min
THUNDERBOLT100K_WEATHER_INTERVAL=5
# The final displayed weather info, default is (condition temp last_update)
# Other supported info names:
#     wind 
THUNDERBOLT100K_WEATHER_INFO=(condition temp last_update)
# Customise the colors (default ones as below)
THUNDERBOLT100K_WEATHER_SUN_COLOR="yellow"
THUNDERBOLT100K_WEATHER_RAIN_COLOR="blue"
THUNDERBOLT100K_WEATHER_CLOUD_COLOR="white"
THUNDERBOLT100K_WEATHER_THUNDER_COLOR="yellow"
THUNDERBOLT100K_WEATHER_OVERCAST_COLOR="grey"
THUNDERBOLT100K_WEATHER_SNOW_COLOR="white"
THUNDERBOLT100K_WEATHER_DEFAULT_COLOR="green"
THUNDERBOLT100K_WEATHER_HIGH_TEMP_COLOR="red"
THUNDERBOLT100K_WEATHER_MIDDLE_TEMP_COLOR="yellow"
THUNDERBOLT100K_WEATHER_LOW_TEMP_COLOR="blue"
THUNDERBOLT100K_WEATHER_UPDATE_TIME_COLOR="red"
# Show the update time if it is longer then given time (in minutes)
THUNDERBOLT100K_WEATHER_SHOW_UPDATE_TIME=120
```

### How it works

As you pip installed, a cmdline tool named `_thunderbolt100k` is registered to the PL9K. Each time you press the 'return' button in the terminal, PL9K will call the `_thunderbolt100k` command.

In this command, it will firstly check if the recorded pid is still exist. If the process is not exist, it will then start a new process to poll the corresponding information. So there is a background process to poll necessary information in every given interval and in the foreground (here is the terminal process), it will take much less time to get the information as it is cached already.

### TODO

1. A script to install all the prerequisites?
2. Should we also contains the specific configuration of PL9K? Or, just the widgets?
3. Check the main process is running each time the PL9K called the entry function