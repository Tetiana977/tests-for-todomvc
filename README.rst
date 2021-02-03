This project includes End-to-End test for proof of concept
web-application TodoMVC. There are also feature tests.

Plan of the testing TodoMVC :
Operations at filter

- all
!!! # create
	# edit
!!!  - by Enter
!    - by Tab
!    - by click outside
!!! # cancel edit (by Escape)
	# delete
!!!  - by click “x”
!!!  - clear completed
!    - edit to “”
!!! # complete
!!  # complete all
!!  # activate
!   # activate all

- active
!!  # create
	# edit
!!   - by Enter
!    - by Tab
!    - by click outside
!!  # cancel edit (by Escape)
	# delete
!!   - by click “x”
!    - clear completed
!    - edit to “”
!!  # complete
!   # complete all
!   # activate all

- completed
!   # create
	# edit
!    - by Enter
!    - by Tab
!    - by click outside
!   # cancel edit (by Escape)
	# delete
!!   - by click “x”
!!   - clear completed
!    - edit to “”
!   # complete all
!!  # activate
!   # activate all

Filters
!!  # all from
     - active
     - completed
!!  # active from
     - completed
     - all
!!  # completed from
     - active
     - all

Items left
!!  # increment
     - create
     - activate
     - activate all
!!  # decrement
     - complete
     - complete all
     - delete active
      ~  by click “x”
      ~ edit to “”
!   # unchange
     - edit
      ~ by Enter
      ~ by Tab
      ~ by click outside
     - clear completed
     - delete completed
     - filters >*


Scenario End-to-End: “Basic todos management”

GIVEN opened TodoMVC
# create “a”,” b”, “c”
assert list: "a", "b", "c"

# cancel edit "c" to "to be canceled"
# delete “c”
assert list: "a", "b"

# edit “a” to “a edited”
# complete "a edited"
# clear completed
assert list: "b"