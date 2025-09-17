#!/usr/bin/awk -f

# Info: This program displays the customer information
# Date: July 17th, 2025
# Version: 1.0
# Author: Velmurugan Kuberan

BEGIN { print "*** Customer Information ***" }
{ print $0 }
END { print "*** Customer Information Ends ***" }

