//
//  ViewController.swift
//  minidriver
//
//  Created by Sandra Adams-Hallie on Jun/6/16.
//  Copyright © 2016 Sandra Adams-Hallie. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    
    @IBOutlet weak var goButton: UIButton!
    @IBOutlet weak var stopButton: UIButton!
    
    @IBAction func goButtonPressed(sender: AnyObject) {
        
        goButton.enabled = false
        stopButton.enabled = true
//        Call to tcp server here
        
    }
    
    @IBAction func stopButtonPressed(sender: AnyObject) {
        stopButton.enabled = false
        goButton.enabled = true
//        Call to tcp server here
    }

    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

}

