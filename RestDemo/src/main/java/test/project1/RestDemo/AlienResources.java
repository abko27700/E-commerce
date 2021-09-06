package test.project1.RestDemo;

import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("aliens")
public class AlienResources {
	
	
	AlienRepository areo=new AlienRepository();
	
	@GET
	@Produces({MediaType.APPLICATION_JSON,MediaType.APPLICATION_XML})
	public List<Alien> getAliens(){
		System.out.println("getAlien cALLLEd");
	
		return areo.getAliens();
	}
	
	@GET
	@Path("alien/{id}") 
	@Produces({MediaType.APPLICATION_JSON,MediaType.APPLICATION_XML})
	public Alien getAlien(@PathParam("id")int id)
	{
		//System.out.println(alien);
		return areo.getAlien(id);
		
	}
	
	@POST
	@Path("alien")
	public Alien createAlien(Alien alien)
	{
		System.out.println(alien);
		areo.create(alien);
		return alien;
	}
}
