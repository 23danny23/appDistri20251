﻿using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using WebApiPerson.Services.Intefaces;
using WebApiPerson.Services.MQ;
using static WebApiPerson.Dtos.EcommerceDtos;

namespace WebApiPerson.Controllers
{

    [ApiController]
    [Route("api/[controller]")]
    public class CategoriesController : ControllerBase
    {
        private readonly ICategoryService _service;
        private readonly RabbitMQService _rabbitMQService;

        public CategoriesController(ICategoryService service, RabbitMQService rabbitMQService)
        {
            _service = service;
            _rabbitMQService = rabbitMQService;
        }

        [HttpGet("ConsularTodo")]
        public async Task<IActionResult> GetCategories()
        {
            return Ok(await _service.ListAsync());
        }

        [HttpGet]
        [Route("id/{id?}")]
        public async Task<IActionResult> GetCategories(string id)
        {
            var response = await _service.GetAsync(id);

            if (!response.Success)
            {
                return NotFound(response);
            }

            return Ok(response);
        }


        [HttpPost]
        public async Task<IActionResult> PostCategories([FromBody] CategoryDto request)
        {
            var response = await _service.CreateAsync(request);
            
            if (response.Success)
            {
                request.Id = response.Result;
                var message = JsonConvert.SerializeObject(request);
                //_rabbitMQService.PublishToQueue("categoriesQueue", message);
            }

            return CreatedAtAction("GetCategories", new
            {
                id = response.Result
            }, response);
        }

        [HttpPost("ingresar")]
        public async Task<IActionResult> IngresarCategoria([FromBody] CategoryDto request)
        {
            var response = await _service.CreateAsync(request);

            if (response.Success)
            {
                request.Id = response.Result;
                var message = JsonConvert.SerializeObject(request);
                _rabbitMQService.PublishToQueue("categoriesQueue", message);
            }

            return Ok(response);
        }


        [HttpPut]
        [Route("{id}")]
        public async Task<IActionResult> PutCategories(string id, [FromBody] CategoryDto request)
        {
            return Ok(await _service.UpdateAsync(id, request));
        }

        [HttpDelete]
        [Route("{id}")]
        public async Task<IActionResult> DeleteCategories(string id)
        {
            var response = await _service.DeleteAsync(id);

            if (response.Success)
            {
                return Ok(response);
            }
            else
            {
                return BadRequest(response);
            }
        }
    }
}
