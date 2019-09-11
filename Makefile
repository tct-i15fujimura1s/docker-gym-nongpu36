IMAGE=jnishii/docker-gym-nongpu-nbgrader

build:
	docker build --force-rm=true -t ${IMAGE} .

run:
	bin/run.sh

save:
	docker save jnishii/docker-gym-nongpu-nbgrader -o gymbox.tar

load:
	docker load -i gymbox.tar

ps:
	docker ps -a

clean:
	rm *~
