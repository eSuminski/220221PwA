package com.revature.logging_basics;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class BasicLogging {

    /*
        log4j is a very common logging framework that we will be using. There are 7 logging levels that go from
        most inclusive to least inclusive:

        ALL: all levels
        DEBUG: designates fine-grained informational events that are most useful to debug an application
        INFO: informational messages that highlight the progress of the application at the coarse grained level
        WARN: designates potentially harmful situations
        ERROR: designates error events that might still allow the application to continue running
        FATAL: severe error events that presumably lead the application to abort
        OFF: highest possible level, intended to turn off logging

        You can determine what levels your logger can include in your log4j2.properties file in your
        resources folder
     */

    static Logger logger = LogManager.getLogger(BasicLogging.class);

    public static void main(String[] args) {
        logger.info("Starting application");

        logger.debug("creating a int variable set to the value of 5"); // if you run this you will not get this logged message
        int x = 5;
        logger.warn("variable x created with a value of 5");

        logger.fatal("application is finished: goodbye!");
    }
}
