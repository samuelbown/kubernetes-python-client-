
## Project chosen

Name: Kubernetes

URL: https://github.com/kubernetes-client/python

Number of lines of code and the tool used to count it: 140,856 counted with Lizard

Programming language: Python

## Coverage measurement

### Existing tool

<Inform the name of the existing tool that was executed and how it was executed>

<Show the coverage results provided by the existing tool with a screenshot>
The coverage tool used by everyone in the group was Coverage.py. Every group member downloaded it on their devices and followed the guide provided on https://coverage.readthedocs.io/en/7.5.3/. After the Kubernetes program was downloaded, a branch test would be run to see the coverage of all tests. The figure below shows the code used and initial coverage that every group member got.  
<br/><br/>  

![initial coverage](https://i.ibb.co/Jky0PS5/Figure-1.png "initial coverage")

Figure 1: Coverage results before any tests implemented


### Your own coverage tool

<The following is supposed to be repeated for each group member>

Name: Samuel

Function 1: “__str__”


Patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements:

https://github.com/samuelbown/kubernetes-python-client-/commit/01f1e191d0396d937b2ecd63dec424571fee44c6



![fig2](https://i.imghippo.com/files/OCaa71719500198.png "fig2")

Figure 2: Coverage tool results for __str__

Function 2: “to_dict”

Patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements:

https://github.com/samuelbown/kubernetes-python-client-/commit/ed7734564a1c1e242926f01c7e1bc15a701dae55

<img src="https://i.ibb.co/JKDtRZq/figure3.png" width="350" height="500">



Figure 3: Coverage tool results for to_dict

Name: Andreas

Function 1: ApiException “__Init__”

Patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements:

https://github.com/samuelbown/kubernetes-python-client-/commit/2f87f80baf489005b1ee9b1be3d607ff1968c370

![fig4](https://i.ibb.co/pnT20fx/figure-4.png "fig4")

Figure 4: Coverage tool results for __Init__

Function 2: DynamicApiError “__str__”

Patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements:

https://github.com/samuelbown/kubernetes-python-client-/commit/8683deee50982506fa3bd6853dc80b167c540d7b

![fig5](https://i.ibb.co/nbrJ6ws/figure-5.png "fig5")

Figure 5: Coverage tool results for __str__

Name: Amelia

Function 1: V1ComponentStatus“__init__”

Patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements:

https://github.com/samuelbown/kubernetes-python-client-/commit/1008bc2f0437fa5d7c7cdcf9daa597c95c4d528e

![fig6](https://i.ibb.co/WBSpPK1/figure-6.png "fig6")

Figure 6: Coverage tool results for __init__


Function 2: V2MetricTarget “__init__”


Patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements:

https://github.com/samuelbown/kubernetes-python-client-/blob/master/kubernetes/client/models/v2_metric_target.py

![fig7](https://i.ibb.co/GR4899n/figure-7.png "fig7")

Figure 7: Coverage tool results for __init__

Name: Chirag

Function 1: ApiException “__init__”

Patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements:

https://github.com/samuelbown/kubernetes-python-client-/commit/7afea5a19169b195e2c7b19a37586b2bbd608e68


<img src="https://i.ibb.co/3r1Ryks/figure-8.png" width="350" height="500">

Figure 8: Coverage tool results for __init__


Function 2: Configuration “get_api_key_with_prefix”


Patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements:

https://github.com/samuelbown/kubernetes-python-client-/commit/2ee7e8d9765268a1f56beb84d393b7fd1f63846c

![fig9](https://i.ibb.co/HFzZyyw/figure-9.png "fig9")

Figure 9: Coverage tool results for get_api_key_with_prefix



## Coverage improvement

### Individual tests


Name: Samuel

1. ApiException “__str__” Tests:

Patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test:

https://github.com/samuelbown/kubernetes-python-client-/commit/a26c32b55d396dea17b34366f521be52d8bf1182

![fig10](https://i.ibb.co/thM0kZ6/figure-10.png "fig10")

Figure 10: Coverage results before the __str__ tests were implemented

![fig11](https://i.ibb.co/zJKHz3c/figure-11.png "fig11")

Figure 11: Coverage results after the __str__ tests were implemented


As seen in the images, by adding tests, the coverage has improved by 7% in test_client.py. The cause of the percentage changes in the other tests is unknown but is also not relevant to this test in particular. After looking into it, we assumed this is some issue with Coverage.py because we have been encountering some problems with it while working on the assignment. The function that was tested had two if-statements as the possible branches, therefore the tests consisted of all combinations of whether they were entered or not.



2. Version Info “to_dict” Tests:

Patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test:

https://github.com/samuelbown/kubernetes-python-client-/commit/d7bc4d90959daef3ec7a51f93a8cc7c9b29dd4ec

![fig12](https://i.ibb.co/tQXXG3r/figure-12.png "fig12")

Figure 12: Coverage results before the to_dict tests were implemented

![fig13](https://i.ibb.co/jfjFDMT/figure-13.png "fig13")

Figure 13: Coverage results after the to_dict tests were implemented


These tests have increased the coverage of the test_client.py file by 6%. The function being tested consisted of 1 if-statement with 4 different branches, so there were tests for each of those branches being executed.

Name: Andreas

1. ApiException “__init__” Tests:

Patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test:

https://github.com/samuelbown/kubernetes-python-client-/commit/28e697bd5dc61b4f87bfe92963e7564f13c24bd4

![fig14](https://i.ibb.co/4sN06Zy/figure-14.png "fig14")

Figure 14: Coverage results before the __init__ tests were implemented

![fig15](https://i.ibb.co/GRvm41c/figure-15.png "fig15")

Figure 15: Coverage results after the __init__ tests were implemented


The coverage of test_client, where the test is, has increased by 3%. There was an if and else statement in the function, so 2 branches that were not covered before now are.

2. DynamicApiError “__str__” Tests:

Patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test:

https://github.com/samuelbown/kubernetes-python-client-/compare/master...dynamic-__str__-tests

![fig16](https://i.ibb.co/YXsdqhn/figure-16.png "fig16")

Figure 16: Coverage results before the __str__ tests were implemented

![fig17](https://i.ibb.co/QNkn6R1/figure-17.png "fig17")

Figure 17: Coverage results after the __str__ tests were implemented


By adding tests to the str function from the DynamicApiError class, 3 if statements, and thus 3 branches, which were not covered before now are, the function is fully covered and the overall coverage of dynamic/test_client has gone up by 4%


Name: Amelia

1. v1_component_status Tests "__init__":

Patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test:

https://github.com/samuelbown/kubernetes-python-client-/commit/4d11ddfc34f9d249c77a0efc6a6320714f401014

![fig18](https://i.ibb.co/fVWqW3V/figure-18.png "fig18")

Figure 18: Coverage results before the __init__ tests were implemented

![fig19](https://i.ibb.co/Wn37VrT/figure-19.png "fig19")

Figure 19:Coverage results after the __init__ tests were implemented

Through the implementation of this test for the v1_component_status "__init__" function, there was a 8% increase in coverage of test_client.py this was due to there being  5 if statements that were not covered previously.


2. v2_metric_target "__init__" Tests:

Patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test:

https://github.com/samuelbown/kubernetes-python-client-/commit/4d11ddfc34f9d249c77a0efc6a6320714f401014

![fig20](https://i.ibb.co/2hJ5qF3/figure-20.png "fig20")

Figure 20: Coverage results before the __init__ tests were implemented

![fig21](https://i.ibb.co/JpXmFqc/figure-21.png "fig21")

Figure 21: Coverage results after the __init__ tests were implemented

Through the implementation of this test for the v2_metric_target "__init__" function, there was a 5% increase in coverage of test_client.py this was due to there being 4 branches that were previously not covered by the tests.


Name: Chirag

1. AdmissionregistrationV1ServiceReference “__init__” Tests:

Patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test:

https://github.com/samuelbown/kubernetes-python-client-/commit/b5d7eeca2dcba878fc26a7b756f2c0978e7e7af6

![fig22](https://i.ibb.co/BnN7yTn/figure-22.png "fig22")

Figure 22: Coverage results before the __init__ tests were implemented

![fig23](https://i.ibb.co/hHQpcS0/figure-23.png "fig23")

Figure 22: Coverage results after the __init__ tests were implemented

The function chosen had 3 “if” statements which weren’t covered. Hence by implementing tests those branches were covered thus the 9% coverage increase in test_client.py.

2. Configuration “get_api_key_with_prefix” Tests:

Patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test:

https://github.com/samuelbown/kubernetes-python-client-/commit/b5d7eeca2dcba878fc26a7b756f2c0978e7e7af6

![fig24](https://i.ibb.co/BnN7yTn/figure-22.png "fig24")

Figure 24: Coverage results before the get_api_key_with_prefix tests were implemented

![fig25](https://i.ibb.co/8Dr2XxH/figure-25.png "fig25")

Figure 25: Coverage results after the get_api_key_with_prefix tests were implemented

This function had 2 if statements, one of them containing a separate if-else statement. By implementing the tests all the possible branches were covered, increasing the branch coverage by 7%.


### Overall

Old coverage results:
![initial coverage](https://i.ibb.co/Jky0PS5/Figure-1.png "initial coverage")

Figure 26: Coverage results with no tests implemented

New coverage results:
![fig27](https://i.ibb.co/1vkTRb8/figure-27.png "fig27")

Figure 27: Coverage results with all tests implemented
## Statement of individual contributions

We had several group meetings to organize what each group member would do. Each group member worked on both parts of the assignment on their own, asking questions if they needed help. Some members had issues with making their tests, so we worked together as a group to help each other. In the end everyone in the group can agree that the work we did was equal, which was the goal that we were striving for.
