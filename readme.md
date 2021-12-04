# Sublime-clean-css

A plugin for [Sublime Text](https://www.sublimetext.com/) providing an interface to [clean-css](https://github.com/clean-css/clean-css).

## Install

You can install via with [Package Control](https://packagecontrol.io/) and restart Sublime.

- **Install Package**: Search with `clean-css`.
- **Add Repository**: Put URL `https://github.com/1000ch/Sublime-clean-css`.

Also you can install this extension locally by putting symbolic link from `~/Library/Application\ Support/Sublime\ Text/Packages/` to `~/path/to/this/repo` like below.

```bash
$ ln -s ~/workspace/github.com/1000ch/Sublime-clean-css ~/Library/Application\ Support/Sublime\ Text/Packages/clean-css
```

### Prerequisite

[clean-css](https://github.com/clean-css/clean-css) requires Node.js as runtime. If you don't have Node.js, I recommend you to install Node.js using version managers like the followings.

- Use [nodenv/nodenv](https://github.com/nodenv/nodenv)
- Use [hokaccha/nodebrew](https://github.com/hokaccha/nodebrew)

## Usage

In a CSS file, open the Command Palette (<kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>P</kbd>) and choose **Format CSS** or **Minify CSS**.

## Config

You can configure [css-clean options](https://github.com/clean-css/clean-css#constructor-options) from Preferences → Package Settings → Clean-css → Settings - User.

## License

[MIT](https://1000ch.mit-license.org) © [Shogo Sensui](https://github.com/1000ch)
