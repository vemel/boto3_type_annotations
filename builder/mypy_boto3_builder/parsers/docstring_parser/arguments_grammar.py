from pyparsing import (
    Forward,
    SkipTo,
    Literal,
    LineEnd,
    Word,
    alphanums,
    indentedBlock,
    Optional,
    White,
)


class ArgumentsGrammar:
    indent_stack = [1]
    EOL = LineEnd().suppress()
    line = SkipTo(LineEnd()) + EOL
    line_indented = Forward()
    any_line = Forward()
    indented_block = indentedBlock(
        line_indented | any_line, indentStack=indent_stack
    ).setResultsName("indented")
    line_indented <<= any_line + indented_block

    type_definition = (
        Literal(":type").suppress()
        + Word(alphanums + "_").setResultsName("name")
        + Literal(":").suppress()
        + SkipTo(EOL).setResultsName("type_name")
    )

    param_definition = (
        Literal(":param").suppress()
        + Word(alphanums + "_").setResultsName("name")
        + Literal(":").suppress()
        + SkipTo(EOL).setResultsName("description")
        + EOL
        + Optional(indented_block)
    )

    typed_dict_key_line = (
        Literal("-")
        + White(ws=" \t")
        + Literal("**")
        + Word(alphanums + "_").setResultsName("name")
        + Literal("**")
        + White(ws=" \t")
        + Literal("*(")
        + Word(alphanums + "_").setResultsName("type_name")
        + Literal(")")
        + White(ws=" \t")
        + Literal("--*")
        + SkipTo(EOL).setResultsName("description")
        + EOL
    )

    type_line = (
        Literal("-")
        + White(ws=" \t")
        + Literal("*(")
        + Word(alphanums + "_").setResultsName("type_name")
        + Literal(")")
        + White(ws=" \t")
        + Literal("--*")
        + SkipTo(EOL).setResultsName("description")
        + EOL
    )

    any_line <<= (typed_dict_key_line | type_line | line).setResultsName("line")

    @classmethod
    def fail_action(
        cls, _input_string: str, _chr_index: int, _source: str, _error: str
    ) -> None:
        return
        # column = col(chr_index, input_string)
        # print(
        #     "fail", column, cls.indent_stack, _error,
        # )
        # if column in cls.indent_stack:
        #     while cls.indent_stack[-1] != column:
        #         cls.indent_stack.pop()

    @classmethod
    def reset(cls) -> None:
        cls.indented_block.setFailAction(cls.fail_action)
        while len(cls.indent_stack) > 1:
            cls.indent_stack.pop()
