import streamlit as st

from bf import BrainFuck

st.write('''
# Just another BrainF-ck compiler:joy:
****
''')
with st.sidebar:
    st.write('''### *BrainF-ck*''')
    st.image('bf.png')
    st.write('''****''')
    st.write('''*[BrainF-ck](https://en.wikipedia.org/wiki/Brainfuck) is one of the most famous esoteric programming languages 
                and it was created by Urban Müller.*''')
    with st.expander("Syntax"):
        st.write('''
        | Syntax | Description |
        | ----------- | ----------- |
        | > | Move memory pointer to the right once |
        | < | Move memory pointer to the left once |
        | + | Increment value at pointer by 1 |
        | - | Decrement value at pointer by 1 |
        | [ | Skip to corresponding ']' if value at pointer is 0 |
        | ] | Skip to corresponding '[' if value at pointer isn't 0 |

        Everything else is considered a comment.
        ''')
st.write('''You can input your BrainF--ck code in the text box and get the output, It's as simple as that.

User input for the program isn't supported yet :disappointed:
''')

code = st.text_area(label='Input code',height=300)
examples = {
    'Hello World' : '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.',
    'Sierpenski Triangle' : '''.++++++++[>+>++++<<-]>++>>+<[-[>>+<<-]+>>]>+[
                                -<<<[
                                    ->[+[-]+>++>>>-<<]<[<]>>++++++[<<+++++>>-]+<<++.[-]<<
                                ]>.>+[>>]>+
                            ]'''
}
A = st.button('Compile')
B = st.selectbox('Run with an example', ('Hello World','Sierpenski Triangle'))
C = st.button('Go')

if A:
    if code:
        with st.spinner('Compiling..'):
            bf = BrainFuck(200)
            try:
                x = bf.compile(code)
            except:
                st.error("An Error has occured.")
            else:
                st.success("Successfully compiled!!")
                st.write('### Output')
                st.text(x)
    else:
        st.error("Enter something before compiling, please.")

if C:
    code = examples[B]
    st.write("Running ", B)
    st.code(code)
    with st.spinner('Compiling..'):
        st.success('Compiled Successfully..')
        st.write('#### Output')
        bf = BrainFuck(200)
        x = bf.compile(code)
        st.text(x)
