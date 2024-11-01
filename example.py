from neatlogger import log

log.new("Welcome to my script")
log.trace("Some minor tracing message")
x = 42
log.debug("Let's debug value x={}", x)
log.info("By the way, it's going well so far.")
log.progress("Heavy calculation ahead...")
log.read("Reading in some data...")
log.write("Writing some output file...")
log.warning("Note that writing files could take some time!")
try:
    x / 0
except Exception as e:
    log.error("An error occured: {}", e)
log.success("Yey, found a solution to the problem eventually.")
log.done("")
