# Minecraft Backup Management
This is an app to help with management of Minecraft saves 
and backups. Not too many features currently exist so send
me some ideas or something

# Current features (v 1.0.0)
- Automatic backup extraction to keep a save constantly
  restored on deletion, useful for speedrunning fixed
  seeds or downloaded maps
- World number tracker for backup extraction
- Backup folder cleanup to get rid of redundant backups
  and free up storage

# How to run
You know what since I figured it out I'll actually be nice
and pull up the installment guide

- Make sure you have python and git installed
- Run the following set of commands in your terminal:
```commandline
git clone https://github.com/tousef-refuge/Minecraft-Backup-Management.git
cd Minecraft-Backup-Management
py -m venv .venv
.venv\Scripts\activate
pip install -e .
```
- You may want to change certain words here depending on your
  OS (for example 'python' instead of 'py') but this is the
  general idea
- Starting from this point, everytime 'directory' is
  mentioned in a box it will refer to the directory of the
  project downloaded onto your computer
- Whenever you want to use the app, run the following in
  your terminal:
```commandline
cd directory
.venv\Scripts\activate
python -m app
```
- If you want a shortcut to the app, create a new shortcut,
  check its properties and edit the following:
```commandline
Target: directory\.venv\scripts\python.exe
Start in: directory
```
- Now everything should work normally

If something doesn't work on other OS, well my bad lmao

# Changelog

- (v 0.1.0) Initial release
- (v 0.2.0) Backup extraction can now be configured
- (v 0.3.0) Added a sound effect that plays when you extract 
  a backup to make sure you don't accidentally open the 
  world while still extracting from it. Also fixed a minor
  bug with world number tracking

- (v 1.0.0) Added backup folder cleanup and a proper
  installment guide
