package com.example.spring5tutorial.mail;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

public class DemoBean {

	private static Log log = LogFactory.getLog(MockMailSender.class);
	
	public DemoBean() {
		log.info("Demo bean created");
	}
	
	

}