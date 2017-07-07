# thunderbolt100k

A collection of interesting widgets to enhance [powerlevel9k](https://github.com/bhilburn/powerlevel9k) theme for ZSH

Build your awesome terminal with [powerlevel9k](https://github.com/bhilburn/powerlevel9k) and this project!

Inspired by [JulienLemonde' Configuration](https://github.com/bhilburn/powerlevel9k/wiki/Show-Off-Your-Config#julienlemonde-configuration) for powerlevel9k.

### Prerequisites

1. Install [Oh My ZSH]
2. Install [powerlevel9k](https://github.com/bhilburn/powerlevel9k) theme
3. Install [nerd-fonts](https://github.com/ryanoasis/nerd-fonts)

### Installation



### Configuration

You can configure the token of https://api.apixu.com, weather location and etc. in `~/.zshrc` file. Here are all the configurations you can set:

```shell
# The token (i.e. api key) for https://api.apixu.com
THUNDERBOLT100K_WEATHER_TOKEN=<ToBeReplaced>
# The city of the weather
THUNDERBOLT100K_WEATHER_CITY=<ToBeReplaced>
# Interval (minutes) to pull the weather info, by default is 5 min
THUNDERBOLT100K_WEATHER_INTERVAL=5
```

### TODO

1. A script to install all the prerequisites?
2. Should we also contains the specific configuration of PL9K? Or, just the widgets?
3. Check the main process is running each time the PL9K called the entry function