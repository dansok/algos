class Rational(m: Int, n: Int) {
	private gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
	private val g = gcd(m, n)

	def numerator = m / g
	def denominator = n / g

	def add(that: Rational): Rational =
		new Rational(numerator * that.denominator + that.numerator * denominator,
			denominator * that.denominator)

	def neg: Rational = new Rational(-numerator, denominator)

	def subtract(that: Rational): Rational = add(that.neg)

	override def toString = numerator + "/" + denominator
}

object PlayGround {
	def main(args: Array[String]): Unit = {
		val q = new Rational(2, 3)
		val r = new Rational(1, 2)
		val t = new Rational(6, 27)
		println(q.add(r))
		println(q.subtract(r))
		println(q.subtract(r).subtract(t))
	}
}