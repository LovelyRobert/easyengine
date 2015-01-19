function ee_single()
{
    for (( j=0; j<${#COMP_WORDS[@]}; j++ )); do
        for (( i=0; i<${#COMPREPLY[@]}; i++ )); do
            if [[ ${COMP_WORDS[COMP_CWORD-j]} == ${COMPREPLY[i]} ]]; then
                rem=( ${COMP_WORDS[COMP_CWORD-j]} );
                COMPREPLY=( "${COMPREPLY[@]/$rem}" )
            fi
        done
    done
}

_ee_complete()
{
    local cur prev BASE_LEVEL

    COMPREPLY=()
    cur=${COMP_WORDS[COMP_CWORD]}
    prev=${COMP_WORDS[COMP_CWORD-1]}
    mprev=${COMP_WORDS[COMP_CWORD-2]}


    # SETUP THE BASE LEVEL (everything after "ee")
    if [ $COMP_CWORD -eq 1 ]; then
        COMPREPLY=( $(compgen \
                      -W "stack site debug clean secure" \
                      -- $cur) )


    # SETUP THE SECOND LEVEL (EVERYTHING AFTER "ee second")
    elif [ $COMP_CWORD -eq 2 ]; then
        case "$prev" in

            # HANDLE EVERYTHING AFTER THE SECOND LEVEL NAMESPACE
            "clean")
                COMPREPLY=( $(compgen \
                              -W "--memcache --opcache --fastcgi --all" \
                              -- $cur) )
                ;;

            # IF YOU HAD ANOTHER CONTROLLER, YOU'D HANDLE THAT HERE
            "debug")
                COMPREPLY=( $(compgen \
                              -W "--start --nginx --php --fpm --mysql -i --interactive" \
                              -- $cur) )
                ;;

            "stack")
                COMPREPLY=( $(compgen \
                              -W "install purge reload remove restart start status stop" \
                              -- $cur) )
                ;;

            "site")
                COMPREPLY=( $(compgen \
                              -W "create delete disable edit enable info list log show update" \
                              -- $cur) )
                ;;

            "secure")
                COMPREPLY=( $(compgen \
                              -W "--auth --port --ip" \
                              -- $cur) )
                ;;

            "info")
                COMPREPLY=( $(compgen \
                              -W "--mysql --php --nginx" \
                              -- $cur) )
                ;;

            # EVERYTHING ELSE
            *)
                ;;
        esac

    # SETUP THE THIRD LEVEL (EVERYTHING AFTER "ee second third")
    elif [ $COMP_CWORD -eq 3 ]; then
        case "$prev" in
            # HANDLE EVERYTHING AFTER THE THIRD LEVEL NAMESPACE
            "install" | "purge" | "remove" | "start" | "stop" | "reload")
                COMPREPLY=( $(compgen \
                              -W "--web --admin --mail --nginx --php --mysql --postfix --wpcli --phpmyadmin --adminer --utils --memcache --dovecot" \
                              -- $cur) )
                ;;

            "list")
                COMPREPLY=( $(compgen \
                              -W "--enabled --disabled" \
                              -- $cur) )
                ;;

            "edit" | "enable" | "info" | "log" | "show" | "cd" | "update")
                COMPREPLY=( $(compgen \
                              -W "$(find /etc/nginx/sites-available/ -type f -printf "%P " 2> /dev/null)" \
                              -- $cur) )
                ;;

            "disable")
                COMPREPLY=( $(compgen \
                              -W "$(command find /etc/nginx/sites-enabled/ -type l -printf "%P " 2> /dev/null)" \
                              -- $cur) )
                ;;

            *)
                ;;
        esac

        # case "$mprev" in
        #     "debug")
        #         COMPREPLY=( $(compgen \
        #                             -W "--wp --nginx --rewrite --start --stop -i --interactive" \
        #                         -- $cur) )
        #     ;;
        #
        #     *)
        #         ;;
        # esac

    elif [ $COMP_CWORD -eq 4 ]; then
        case "$mprev" in
            # HANDLE EVERYTHING AFTER THE THIRD LEVEL NAMESPACE

            "create" | "update")
                COMPREPLY=( $(compgen \
                                    -W "--html --php --mysql --wp  --wpsubdir --wpsubdomain --w3tc --wpfc --wpsc" \
                                 -- $cur) )
                ;;
            "delete")
                COMPREPLY=( $(compgen \
                                    -W "--db --files --all" \
                                 -- $cur) )


        esac
    fi

    case "$prev" in
        "--wpsubdir" | "--wpsubdomain")
            COMPREPLY=( $(compgen \
                          -W "--w3tc --wpfc --wpsc" \
                          -- $cur) )
            ;;

        "--web" | "--admin" | "--mail" | "--nginx" | "--php" | "--mysql" | "--postfix" | "--wpcli" | "--phpmyadmin" | "--adminer" | "--utils" | "--memcache" | "--dovecot")
            if [[ $COMP_WORDS =~ "stack" ]]; then
                retlist="--web --admin --mail --nginx --php --mysql --postfix --wpcli --phpmyadmin --adminer --utils --memcache --dovecot"
                ret="${retlist[@]/$prev}"
                COMPREPLY=( $(compgen \
                            -W "$(echo $ret)" \
                            -- $cur) )
            fi
            ;;

        "--db" | "--files" | "--all")
            retlist="--db --files --all"
            ret="${retlist[@]/$prev}"
            COMPREPLY=( $(compgen \
                          -W "$(echo $ret)" \
                          -- $cur) )
            ;;

        "--memcache" | "--opcache" | "--fastcgi" | "--all")
            retlist="--memcache --opcache --fastcgi --all"
            ret="${retlist[@]/$prev}"
            COMPREPLY=( $(compgen \
                          -W "$(echo $ret)" \
                          -- $cur) )
            ;;
        "--auth" | "--port" | "--ip")
            retlist="--auth --port --ip"
            ret="${retlist[@]/$prev}"
            COMPREPLY=( $(compgen \
                          -W "$(echo $ret)" \
                          -- $cur) )
            ;;
        *)
            ;;
        esac

    return 0

} &&
complete -F _ee_complete ee
