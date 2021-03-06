# VeggieIpsum

An extension for Sublime Text 2 and 3!

It allow you to Insert Veggie Ipsum in the editor via menu items or keyboard shortcut.

Select how much text you want from the menu item in `Edit->Text->Veggie Ipsum` or on the right click menu in `Veggie Ipsum`.

Just press the shortcut key (Alt+Shift+L) to add Veggie Ipsum text. Keep pressing to add more.

Alternatively, you can also specify the number of paragraphs, by writing a number, and pressing the shortcut key. Veggie Ipsum will check if there is a number directly preceding the selection range, and replace it with that many paragraphs of Veggie ipsum. Addind a decimal point, defines the approximate number of words per paragraph.

## Examples

Generate a dummy title for a blog, and a few paragraphs

- Press the shortcut once, to generate a single line of Veggie upsum, of about 10 characters
- Move down to a newline, and type `5.60` and then press the keyboard shortcut for Veggie ipsum

## Features

1. Uses only words from [the original Veggie ipsum text](http://www.lipsum.com/)
2. Randomly generates text from selection of words
3. Always starts with `Veggie ipsum` for first paragraph, and capitalizes following paragraphs
4. Leaves the inserted text un-selected, so you can insert some more straight away (rapid tapping to get as much Veggie as you want)
5. Shortcut key, `Edit -> Text -> Veggie Ipsum...` sub-menu, and context menu activation
6. Variable size of text from just `a bit` to more than you can shake a stick at!
7. Specify how many paragraphs and words per paragraph you want (type a number before pressing the Veggie ipsum keyboard shortcut)
8. Works with multiple selection ranges
9. Does not leave trailing spaces

## Install

### Package Control

The easiest way to install this is with [Package Control](http://wbond.net/sublime\_packages/package\_control).

 * If you just went and installed Package Control, you probably need to restart Sublime Text before doing this next bit.
 * Bring up the Command Palette (Command+Shift+P on OS X, Control+Shift+P on Linux/Windows).
 * Select "Package Control: Install Package" (it'll take a few seconds)
 * Select VeggieIpsum when the list appears.

Package Control will automatically keep Git up to date with the latest version.

Report bugs here, and I will do my best to repair them (or better still - make the fix, and send me a pull request).

---

If you have some problems or improvements with it, contact me via GitHub.
