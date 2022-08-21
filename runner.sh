
#!/bin/bash
value=$(cat newtest.csv | fzf --header-lines=1 --reverse --pointer='->' -i --color='hl:bright-red,hl:bold,hl:underline' --exact -d ',' --with-nth=1,3,4  )

echo $value
blue=$(echo "$value" | awk -F ',' '{print $2}' )
mpv --volume=50 $blue
