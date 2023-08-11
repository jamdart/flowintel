# Flowintel-cm

A flexible case management.

![case-management](https://github.com/flowintel/flowintel-cm/blob/main/doc/case_fcm.png?raw=true)

![task-management](https://github.com/flowintel/flowintel-cm/blob/main/doc/task_fcm.png?raw=true)

## Installation

```
./install.sh
./launch.sh -i # To init the db\
./launch.sh -l
```

## Configuration

Go to `config.py` and change just like you want to.

## Account

- email: `admin@admin.admin`

- password: `admin`

After login go to `Users->New User` and create a new user with admin right. Then go back to `Users` and delete `admin` user

## Screen

A screen is created to notify recurrent case. To access it:

```bash
screen -r fcm
```

## Api

`/api/case/doc`

`/api/admin/doc`
