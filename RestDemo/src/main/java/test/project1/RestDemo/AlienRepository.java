package test.project1.RestDemo;

import java.util.ArrayList;
import java.util.List;

public class AlienRepository {
	 List<Alien> aliens;

	public  AlienRepository() {

		aliens=new ArrayList<Alien>();
		Alien a1 = new Alien();
		a1.setName("Abhishek");
		a1.setPoints(60);
		a1.setId(1);

		Alien a2 = new Alien();
		a2.setName("Deepak");
		a2.setPoints(61);
		a2.setId(2);
		aliens.add(a1);
		aliens.add(a2);
		
	}

	public List<Alien> getAliens() {
		return aliens;
	}

	public Alien getAlien(int id) {
		for (Alien a : aliens) {
			if (a.getId() == id) {
				return a;
			}
		}
		return null;
	}

	public void create(Alien alien) {
		aliens.add(alien);
		
	}
}
