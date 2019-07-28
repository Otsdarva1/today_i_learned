package com.example.spring5tutorial.controller;

import javax.mail.MessagingException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.spring5tutorial.mail.MailSender;

@RestController
public class MailController {

	private MailSender mailSender;

	public MailController(MailSender smtp) {
		this.mailSender = smtp;
	}
	
	@RequestMapping("/mail")
	public String hello() throws MessagingException {
		
		mailSender.send("yamazaki192748@gmail.com", "A test mail", "Body of the test mail");
		return "Mail Sent";
	}

}
