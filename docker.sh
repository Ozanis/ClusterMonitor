docker_setup(side, img){
	path="$(pwd)/${side}"
	cd ${path}
	docker build . -t ${img}
	docker images
	docker -run --name daemon -d ubuntu ${img} -c
}


if [[$(whoami) -ne "root"]] then
	echo "You should be a root"
	exit 0;
fi

if [[-z "`pacman -Qs docker`"]] then 
	pacman -S docker
fi

read -p "Which service would ypu like to run (Client or Server)? Please type c/sto answer" choice

case in ${choice}
	"S"|"s") docker_setup("Server/", "server_image");;
	"C"|"c") docker_setup("Agent/", "client_image");;
	*) echo "Cacncel option have been chocen"
		exit 0;;
esac





