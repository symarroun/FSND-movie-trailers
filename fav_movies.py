import media
import fav_movies_web

# Instances of my favorite movies:

deadpool = media.Movie("Deadpool",
						"Wade Wilson (Ryan Reynolds) is a former Special Forces operative"
						"who now works as a mercenary. His world comes crashing down when "
						"evil scientist Ajax (Ed Skrein) tortures, disfigures and transforms"
						"him into Deadpool. The rogue experiment leaves Deadpool with"
						"accelerated healing powers and a twisted sense of humor. With help from"
						"mutant allies Colossus and Negasonic Teenage Warhead (Brianna "
						"Hildebrand), Deadpool uses his new skills to hunt down the man who"
						"nearly destroyed his life.",
						"https://www.flickeringmyth.com/wp-content/uploads/2016/01/Deadpool-poster-1.jpg",  # NOQA
						"https://www.youtube.com/watch?v=Xithigfg7dA")  # NOQA

focus = media.Movie("Focus",
						"Nicky (Will Smith), a veteran con artist, takes a novice named Jess"
						"(Margot Robbie) under his wing. While Nicky teaches Jess the tricks"
						"of the trade, the pair become romantically involved; but, when Jess"
						"gets uncomfortably close, Nicky ends their relationship.",
						"http://static.rogerebert.com/uploads/movie/movie_poster/focus-2015/large_focus_ver2.jpg",  # NOQA
						"https://www.youtube.com/watch?v=MxCRgtdAuBo")  # NOQA

mechanic = media.Movie("Mechanic: Resurrection",
						"Living under cover in Brazil, master assassin Arthur Bishop"
						"(Jason Statham) springs back into action after an old enemy"
						"Sam Hazeldine) kidnaps the woman (Jessica Alba) he loves. To save"
						"her life, Bishop must kill an imprisoned African warlord, a human"
						"trafficker (Toby Eddington) and an arms dealer (Tommy Lee Jones),"
						"all while making the deaths look like accidents. When things don't go"
						"exactly as planned, Bishop turns the tables on the people who forced"
						"him out of retirement.",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BMjYwODExNzUwMV5BMl5BanBnXkFtZTgwNTgwNjUyOTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
						"https://www.youtube.com/watch?v=G-P3f_wDXvs")  # NOQA

enemy = media.Movie("Enemy",
						"A mild-mannered college professor (Jake Gyllenhaal)"
						"discovers a look-alike actor and delves into the other"
						"man's private affairs.",
						"http://www.impawards.com/intl/misc/2014/posters/enemy.jpg",  # NOQA
						"https://www.youtube.com/watch?v=FJuaAWrgoUY")  # NOQA

wonder_woman = media.Movie("Wonder Woman",
						"Before she was Wonder Woman (Gal Gadot), she was Diana, princess of"
						"the Amazons, trained to be an unconquerable warrior. Raised on a"
						"sheltered island paradise, Diana meets an American pilot (Chris Pine)"
						"who tells her about the massive conflict that's raging in the outside"
						"world. Convinced that she can stop the threat, Diana leaves her"
						"home for the first time. Fighting alongside men in a war to end all"
						"wars, she finally discovers her full powers and true destiny.",
						"http://cdn2-www.comingsoon.net/assets/uploads/gallery/wonder-woman/wwposter5.jpg",  # NOQA
						"https://www.youtube.com/watch?v=1Q8fG0TtVAY")  # NOQA

ghost_in_the_shell = media.Movie("Ghost in the Shell",
						"In the near future, Major is the first of her kind: a human who is"
						"cyber-enhanced to be a perfect soldier devoted to stopping the"
						"world's most dangerous criminals. When terrorism reaches a new"
						"level that includes the ability to hack into people's minds and"
						" control them, Major is uniquely qualified to stop it. As she"
						"prepares to face a new enemy, Major discovers that her life was stolen"
						"instead of saved. Now, she will stop at nothing to recover her past"
						"while punishing those who did this to her.",
						"http://cdn2-www.comingsoon.net/assets/uploads/gallery/ghost-in-the-shell/ghostinshellposter.jpg",  # NOQA
						"https://www.youtube.com/watch?v=G4VmJcZR0Yg")  # NOQA

# All instances grouped together in a list
movies = [deadpool, focus, mechanic, enemy, wonder_woman, ghost_in_the_shell]
fav_movies_web.open_movies_page(movies)   # the array/list is inputed as an argument