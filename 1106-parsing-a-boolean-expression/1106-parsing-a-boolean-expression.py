class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        while len(expression) > 1:
            start = max(
                expression.rfind("!"),
                expression.rfind("&"),
                expression.rfind("|"),
            )
            end = expression.find(")", start)
            sub_expr = expression[start : end + 1]
            result = self._evaluate_sub_expr(sub_expr)
            expression = expression[:start] + result + expression[end + 1 :]

        return expression == "t"

    def _evaluate_sub_expr(self, sub_expr: str) -> str:
        op = sub_expr[0]
        values = sub_expr[2:-1]

       
        if op == "!":
            return "f" if values == "t" else "t"
        if op == "&":
            return "f" if "f" in values else "t"
        if op == "|":
            return "t" if "t" in values else "f"

        return "f"  