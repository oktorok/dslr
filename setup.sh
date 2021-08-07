#!/bin/sh

echo "setuping"

HOME=$(echo ~)
PYTHON_PATH=$(which python)
REQUIREMENTS="jupyter numpy pandas matplotlib"

# 42 AI bootcamp installation
if [ "$(uname)" == "Darwin" ]; then

    INSTALL_PATH="/goinfre/$USER"
    MINICONDA_PATH=$INSTALL_PATH"/miniconda3/bin"
    
    SCRIPT="Miniconda3-latest-MacOSX-x86_64.sh"

    DL_LINK="https://repo.anaconda.com/miniconda/"$SCRIPT

	echo "Mac OS"

	if echo $PYTHON_PATH | grep -q $INSTALL_PATH; then
	    echo "good python version :)"
		conda update conda
		#checking requirements
		conda install -y $(echo $REQUIREMENTS)
    else
		cd
		if [ ! -f $SCRIPT ]; then
			curl -LO $DL_LINK
    	fi
		#installing conda sh Script -b -p <path>
    	if [ ! -d $MINICONDA_PATH ]; then
	    	sh $SCRIPT -b -p $INSTALL_PATH"/miniconda3"
		fi

		#installing requirements
		conda install -y $(echo $REQUIREMENTS)
		clear
		echo "Which python: $(which python)"
		
		#exporting path to be able to work on any mac in cluster
		if grep -q "^export PATH=$MINICONDA_PATH" ~/.zshrc
		then
			echo "export already in .zshrc";
		else
			echo "adding export to .zshrc ...";
			echo "export PATH=$MINICONDA_PATH:\$PATH" >> ~/.zshrc
		fi
		source ~/.zshrc
    fi

elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then

    INSTALL_PATH="~"
    MINICONDA_PATH=$INSTALL_PATH"/miniconda3/bin"

    SCRIPT="Miniconda3-latest-Linux-x86_64.sh"
    
    DL_LINK="https://repo.anaconda.com/miniconda/"$SCRIPT

	echo "Linux"

	if echo $PYTHON_PATH | grep -q $INSTALL_PATH; then
	    echo "good python version :)"
		conda update conda
		#checking requirements
		conda install -y $(echo $REQUIREMENTS)
		
	else
		cd
		if [ ! -f $SCRIPT ]; then
			wget $DL_LINK
			chmod +x $SCRIPT
    	fi

		#installing conda sh Script -b -p <path>
    	if [ ! -d $MINICONDA_PATH ]; then
	    	sh $SCRIPT -b -p $INSTALL_PATH"/miniconda3"
		fi
		
		#installing requirements
		conda install -y $(echo $REQUIREMENTS)
		clear
		echo "Which python: $(which python)"
		
		#exporting path to be able to work on any mac in cluster
		if grep -q "^export PATH=$MINICONDA_PATH" ~/.zshrc
		then
			echo "export already in .zshrc";
		else
			echo "adding export to .zshrc ...";
			echo "export PATH=$MINICONDA_PATH:\$PATH" >> ~/.zshrc
		fi
		source ~/.zshrc
	fi
fi
