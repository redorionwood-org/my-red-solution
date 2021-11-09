#!/bin/bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
#

# IGNORED RULES
# E0401 Unable to import module (packaged via Lambda layers instead)
# C0103 Constant name
# C0114 Missing module docstring (missing-module-docstring)
# C0116 Missing function or method docstring (missing-function-docstring)
# C0301 Line too long
# C0302 Too many lines in module
# C0303 Trailing whitespace
# C0411 Order of import
# C0412 Grouping of import
# C0413 Wrong import position (in unit tests)
# R0201 Method could be a function (in unit tests)
# R0801 Similar lines in files
# R1702 Too many nested blocks
# R0912 Too many branches
# R0913 Too many arguments
# R0914 Too many local variables
# R0915 Too many statements
# W0105 No effect string (comment in test)
# W0401 Wildcard import
# W0603 Global statement
# W0621 Redefining name
# W0611 Unused import
# W0613 Unused argument (like passing 'event' or 'context' into lambda)
# W0640 Cell variable
# W0703 Catching too general exception

set -euo pipefail

find . -iname '*.py' | \
    grep "/package/" --invert-match | \
    grep "/chalice/vendor/" --invert-match | \
    xargs pylint -d E0401,C0103,C0114,C0116,C0301,C0302,C0303,C0411,C0412,C0413,R0201,R0801,R1702,R0912,R0913,R0914,R0915,W0105,W0401,W0603,W0611,W0613,W0621,W0640,W0703
