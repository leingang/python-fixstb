import pytest

from fixstb import fixstb


@pytest.mark.parametrize("test_input,expected",[
    (
        r"<p>$\forall x \in \mathbb{Z}$, $\exists y \in \mathbb{Z}$, $y &gt; x$</p>",
        r'<p><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>∀</mo><mi>x</mi><mo>∈</mo><mi mathvariant="double-struck">Z</mi></mrow></math>, <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>∃</mo><mi>y</mi><mo>∈</mo><mi mathvariant="double-struck">Z</mi></mrow></math>, <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>y</mi><mo>></mo><mi>x</mi></mrow></math></p>'
    ),
    (
        r'<p>Suppose $n$ is an integer and $n \geq 1$.&nbsp; Consider the set $A$ of ordered pairs $(i,j)$ where $i$ and $j$ are drawn from $\{1,2,\dots,n\}$ and $i &lt;&nbsp;j$.&nbsp; Count the elements of $A$ two ways to prove combinatorially that $$1 + 2 + \dots + (n-1) = \frac{n(n-1)}{2}$$.<br>&nbsp;</p>',
        r'<p>Suppose <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>n</mi></mrow></math> is an integer and <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>n</mi><mo>≥</mo><mn>1</mn></mrow></math>.  Consider the set <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>A</mi></mrow></math> of ordered pairs <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo stretchy="false">(</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo stretchy="false">)</mo></mrow></math> where <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>i</mi></mrow></math> and <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>j</mi></mrow></math> are drawn from <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo stretchy="false">{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>…</mo><mo>,</mo><mi>n</mi><mo stretchy="false">}</mo></mrow></math> and <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>i</mi><mo><</mo><mi>j</mi></mrow></math>.  Count the elements of <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>A</mi></mrow></math> two ways to prove combinatorially that <math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>…</mo><mo>+</mo><mo stretchy="false">(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo><mo>=</mo><mfrac><mrow><mi>n</mi><mo stretchy="false">(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></math>.<br> </p>'
    )
])
def test_fixstb(test_input, expected):
    assert fixstb(test_input) == expected